from flask import Flask, render_template, jsonify
import one_ql as QL

app = Flask("My QL Server")

human = QL.QlType("human", [
	QL.QlProperty("name", str, False),
	QL.QlProperty("age", int, False),
])
mutation = None
query = QL.QlQuery("Query", [
	QL.Ql_statement("findHuman", human, parameters=[QL.QlProperty("id", int, False)]),
	QL.Ql_statement("humans", human)
])
data = [{"name": "Jaipal", "age": 20, "id": 1}, {"name": "Hema", "age": 21, "id": 2}]
qRes = {
	"findHuman": lambda args: [d for d in data if d["id"] == args["id"]],
	"humans": lambda: data
}
resolver = QL.Resolver(query)
resolver.addResolver(qRes)
server = QL.QlServer(resolver)
# print(server.fetch(QL.QueryReq({"Query": {"findHuman": ["name"]}}), {"id": 1}))

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/types")
def types():
	# return app.response_class(
	# 	response= jsonify(
	# 		Query= {"properties": query.dict()["properties"] if query is not None else []},
	# 		Mutation= {"properties": mutation.dict()["properties"] if mutation is not None else []},
	# 	).data,
	# 	mimetype="application/json",
	# 	content_type="application/json"
	# )
	return app.response_class(
		response=jsonify(
			Query= {"properties": query.dict()["properties"] if query is not None else []},
			Mutation= {"properties": mutation.dict()["properties"] if mutation is not None else []}
		).data,
		mimetype="application/json",
		content_type="application/json"
	)