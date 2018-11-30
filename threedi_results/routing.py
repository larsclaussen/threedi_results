from starlette.routing import Mount, Route, Router
from views import homepage, flow_results

from starlette.schemas import SchemaGenerator, OpenAPIResponse

app = Router([
    Route('/', endpoint=homepage, methods=['GET']),
    Route('/flow_velocity', endpoint=flow_results, methods=['GET']),
])

app.schema_generator = SchemaGenerator(
    {"openapi": "3.0.0", "info": {"title": "Example API", "version": "1.0"}}
)


def schema(request):
    return OpenAPIResponse(app.schema)

app.add_route("/schema", endpoint=schema, methods=["GET"], include_in_schema=False)
