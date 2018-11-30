# -*- coding: utf-8 -*-

"""Main module."""
import asyncio
import datetime


from starlette.responses import JSONResponse
from threedigrid.admin.gridresultadmin import GridH5ResultAdmin
from starlette.schemas import OpenAPIResponse
from starlette.applications import Starlette
from starlette.schemas import SchemaGenerator, OpenAPIResponse

app = Starlette()
app.schema_generator = SchemaGenerator(
    {"openapi": "3.0.0", "info": {"title": "Example API", "version": "1.0"}}
)

gridadmin_f = '/srv/threedi_results/api/gridadmin.h5'
results_f = '/srv/threedi_results/api/results_3di.nc'


async def _fetch(indexes, var_name, model_name):
    print('received flow indexes %s ' %indexes)
    gr = GridH5ResultAdmin(gridadmin_f, results_f)
    t = getattr(gr, model_name).timeseries(indexes=indexes)
    data = t.only(var_name).data
    return data[var_name].tolist()


@app.route('/results/{model_name}/{indexes}/{name}', methods=["GET"])
async def flow_results(request):
    """
    responses:
      200:
        description: time slices of flow velocity.
        examples:
          [{"username": "tom"}, {"username": "lucy"}]
    """

    name = request.path_params['name']
    indexes = request.path_params['indexes']
    model_name = request.path_params['model_name']
    print(indexes)
    indexes_list = [list(map(int, indexes.split(',')))]

    tasks = []
    loop = asyncio.get_event_loop()
    t0 = datetime.datetime.now()
    for indexes in indexes_list:
        print('Start getting indexes "%s"' % indexes)
        # Launch a coroutine for each URL fetch
        # task = loop.create_task(fetch(url, session))
        task = loop.create_task(_fetch(indexes, name, model_name))
        tasks.append(task)

    # Wait on, and then gather, all responses
    flow_data = await asyncio.gather(*tasks)
    dt = (datetime.datetime.now() - t0).total_seconds()
    print('elapsed time: {} [s]'.format(dt))

    return JSONResponse({name: flow_data})


@app.route("/results/{model_name}", methods=["GET"])
def list_result_options(request):
    """
    responses:
      200:
        description: A list of result options per model type.
    """
    gr = GridH5ResultAdmin(gridadmin_f, results_f)
    return JSONResponse(gr.nodes._meta.get_fields(only_names=True))

@app.route('/flow_velocity/')
async def flow_results(request):
    """
    responses:
      200:
        description: time slices of flow velocity.
        examples:
          [{"username": "tom"}, {"username": "lucy"}]
    """

    indexes_list = [[2,3,4,5], [6,7,8,9], [10,11,12,13]]

    tasks = []
    loop = asyncio.get_event_loop()
    t0 = datetime.datetime.now()
    for indexes in indexes_list:
        print('Start getting indexes "%s"' % indexes)
        # Launch a coroutine for each URL fetch
        # task = loop.create_task(fetch(url, session))
        task = loop.create_task(_flow(indexes))
        tasks.append(task)

    # Wait on, and then gather, all responses
    flow_data = await asyncio.gather(*tasks)
    dt = (datetime.datetime.now() - t0).total_seconds()
    print('elapsed time: {} [s]'.format(dt))

    return JSONResponse({'flow_velocity': flow_data})

@app.route('/')
async def homepage(request):
    return JSONResponse({'hello': 'world'})


@app.route("/schema", methods=["GET"], include_in_schema=False)
def schema(request):
    return JSONResponse(app.schema)

