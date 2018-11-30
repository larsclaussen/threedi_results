# -*- coding: utf-8 -*-

"""Main module."""
import asyncio
import datetime


from starlette.applications import Starlette
from starlette.responses import JSONResponse
import uvicorn
from threedigrid.admin.gridresultadmin import GridH5ResultAdmin
from starlette.schemas import OpenAPIResponse


gridadmin_f = '/srv/threedi_results/gridadmin.h5'
results_f = '/srv/threedi_results/results_3di.nc'



async def _flow(indexes):
    print('received flow indexes %s ' %indexes)
    gr = GridH5ResultAdmin(gridadmin_f, results_f)
    t = gr.nodes.timeseries(indexes=indexes)
    data = t.only('s1').data
    return data['s1'].tolist()


async def flow_results(request):

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


async def homepage(request):
    return JSONResponse({'hello': 'world'})


