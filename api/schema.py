import graphene
from graphene import relay
from graphene_django.types import DjangoObjectType, ObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay import from_global_id

from dashboard.models import DecisionTree, Node
from pages.models import PublishedTree
from users.models import CustomUser
from django.conf import settings
from django.utils.text import slugify
import opendecision.schema as api
import json
# user = CustomUser.objects.get(email=settings.API_TEST_USER_MAIL)
# user=info.context.user
# class SchemaQuery(ObjectType):
#     x = String()

#     def resolve_x(root, info):
#         return json.dumps(api.schema.introspect())

class DecisionTreeNode(DjangoObjectType):
    class Meta:
        model = DecisionTree
        filter_fields = '__all__'
        fields = ('created_at', 'name', 'owner', 'slug', 'node_set', 'tags', 'extra_data')
        interfaces = (relay.Node, )

    @classmethod
    def get_queryset(cls, queryset, info):
        if not info.context.user.is_authenticated:
            raise Exception('Authentication credentials were not provided')
        return queryset.filter(owner=info.context.user)

class NodeNode(DjangoObjectType):
    class Meta:
        model = Node
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'slug': ['exact', 'icontains', 'istartswith'],
            'question': ['exact', 'icontains', 'istartswith'],
            'inputs': ['exact', 'icontains', 'istartswith'],
            'decision_tree': ['exact'],
            'start_node': ['exact'],
            'new_node': ['exact'],
            'end_node': ['exact']
                }
        fields = (
            'created_at',
            'name',
            'slug',
            'decision_tree',
            'path',
            'question',
            'inputs',
            'new_node',
            'start_node',
            'end_node',
            'extra_data'
            )
        interfaces = (relay.Node, )

    @classmethod
    def get_queryset(cls, queryset, info):
        if not info.context.user.is_authenticated:
            raise Exception('Authentication credentials were not provided')
        return queryset.filter(decision_tree__owner=info.context.user)

class Query(graphene.ObjectType):
    # get_schema = SchemaQuery

    decision_tree = relay.Node.Field(DecisionTreeNode)
    all_decision_trees = DjangoFilterConnectionField(DecisionTreeNode)

    node = relay.Node.Field(NodeNode)
    all_nodes = DjangoFilterConnectionField(NodeNode)

    # user = relay.Node.Field(UserNode)


class UpdateDecisionTreeMutation(relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)
        tags = graphene.String()
        extra_data = graphene.String()
        id = graphene.ID(required=True)

    tree = graphene.Field(DecisionTreeNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, name, id, **kwargs):
        if not info.context.user.is_authenticated:
            raise Exception('Authentication credentials were not provided')
        try:
            extra_data = kwargs.pop('extra_data')
        except:
            extra_data = ""
        try:
            tags = kwargs.pop('tags')
        except:
            tags = ""
        try:
            tree = DecisionTree.objects.filter(owner=info.context.user).get(id=from_global_id(id)[1])
            tree.name = name
            if extra_data:
                tree.extra_data = extra_data
            if tags:
                tree.tags = tags
            tree.save()
            return UpdateDecisionTreeMutation(tree=tree)
        except:
            raise Exception('Tree does not exist')

class CreateDecisionTreeMutation(relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)
        tags = graphene.String()
        extra_data = graphene.String()

    tree = graphene.Field(DecisionTreeNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, name, **kwargs):
        if not info.context.user.is_authenticated:
            raise Exception('Authentication credentials were not provided')
        try:
            extra_data = kwargs.pop('extra_data')
        except:
            extra_data = ""
        try:
            tags = kwargs.pop('tags')
        except:
            tags = ""
        
        tree = DecisionTree(
            name=name,
        )
        tree.slug=slugify(name)
        tree.owner = info.context.user
        if extra_data:
            tree.extra_data = extra_data
        if tags:
            tree.tags = tags
        tree.save()
        return CreateDecisionTreeMutation(tree=tree)    


class Mutation(graphene.ObjectType):
    update_tree = UpdateDecisionTreeMutation.Field()
    create_tree = CreateDecisionTreeMutation.Field()
