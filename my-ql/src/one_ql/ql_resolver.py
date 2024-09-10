from .ql_query import *

class Resolver:
	def __init__(self, query: QlQuery = None, mutation: QlQuery = None):
		self.query = query
		self.mutation = mutation
		if query is not None and query.name != "Query":
			raise Exception("Root query must be named 'Query'")
		if mutation is not None and mutation.name != "Mutation":
			raise Exception("Root query must be named 'Mutation'")
		self.resolve: dict[str, dict[str, callable]] = {}

	def __getitem__(self, name: str):
		return self.resolve[name]

	def addResolver(self, queryResolver: dict[str, callable] = None, mutationResolver: dict[str, callable] = None):
		self.resolve["Query"] = {}
		self.resolve["Mutation"] = {}
		if queryResolver is None and mutationResolver is None:
			raise Exception("Resolvers must not be None")
		if queryResolver is None and self.query is not None:
			raise Exception("Resolvers must not be None")
		if mutationResolver is None and self.mutation is not None:
			raise Exception("Resolvers must not be None")
		if self.query is not None:
			for i in range(len(queryResolver.items())):
				if list(queryResolver.keys())[i] == self.query.properties[i].name:
					self.resolve["Query"][list(queryResolver.keys())[i]] = list(queryResolver.values())[i]
		if self.mutation is not None:
			for i in range(len(mutationResolver.items())):
				if list(mutationResolver.keys())[i] == self.mutation.properties[i].name:
					self.resolve["Mutation"][list(mutationResolver.keys())[i]] = list(mutationResolver.values())[i]
