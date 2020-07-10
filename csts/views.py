from django.shortcuts import render
from graph_tool.all import *
from django.http import HttpResponse
from .forms import IndexForm
from .models import Port, TransportEdge
from collections import OrderedDict


def index(request):
    if request.method == "POST":
        index_form = IndexForm(request.POST)
        port_name_in = Port.objects.get(id=index_form.data["in_port"])
        port_name_out = Port.objects.get(id=index_form.data["out_port"])
        eqp_len = float(index_form.data["eqp_len"])
        eqp_width = float(index_form.data["eqp_width"])
        eqp_height = float(index_form.data["eqp_height"])
        m3 = eqp_len * eqp_width * eqp_height

        g = graph_tool.Graph(directed=True)

        ports = Port.objects.all()

        transportedges = TransportEdge.objects.all()

        v_prp_id = g.new_vertex_property('string', 'id')
        v_prp_name = g.new_vertex_property('string', 'name')
        v_prp_cost_up = g.new_vertex_property('int', 'cost_in')
        v_prp_cost_down = g.new_vertex_property('int', 'cost_out')
        e_prp_line = g.new_edge_property('string', 'line')
        e_prp_cost = g.new_edge_property('int', 'cost')
        e_prp_td = g.new_edge_property('int', 'travel_day')

        vertices = {}
        for port in ports:
            v = g.add_vertex()
            v_prp_id[v] = port.id
            vertices[port.id] = v
            v_prp_name[v] = port.port_name
            v_prp_cost_up[v] = port.cost_up
            v_prp_cost_down[v] = port.cost_down
        for transportedge in transportedges:
            edg = g.add_edge(vertices[transportedge.source_port.id], vertices[transportedge.target_port.id])
            e_prp_line[edg] = transportedge.line_name
            e_prp_cost[edg] = transportedge.cost_line
            e_prp_td[edg] = transportedge.travel_day

        paths = all_paths(g, g.vertex_index[vertices[int(index_form.data["in_port"])]],
                          g.vertex_index[vertices[int(index_form.data["out_port"])]], edges=True)

        my_dict_from_g = dict()
        my_total_cost = dict()
        my_total_trday = dict()
        for k, path in enumerate(paths, start=1):
            my_dict_from_g[k] = dict()
            j = 1
            for i, elem in enumerate(path):
                my_dict_from_g[k][j] = dict()
                my_dict_from_g[k][j]['type'] = 'port'
                my_dict_from_g[k][j]['status'] = 'up'
                my_dict_from_g[k][j]['name'] = v_prp_name[elem.source()]
                my_dict_from_g[k][j]['cost'] = v_prp_cost_up[elem.source()]
                j += 1
                my_dict_from_g[k][j] = dict()
                my_dict_from_g[k][j]['type'] = 'line'
                my_dict_from_g[k][j]['name'] = e_prp_line[elem]
                my_dict_from_g[k][j]['cost'] = e_prp_cost[elem]
                my_dict_from_g[k][j]['trday'] = e_prp_td[elem]
                j += 1
                my_dict_from_g[k][j] = dict()
                my_dict_from_g[k][j]['type'] = 'port'
                my_dict_from_g[k][j]['status'] = 'down'
                my_dict_from_g[k][j]['name'] = v_prp_name[elem.target()]
                my_dict_from_g[k][j]['cost'] = v_prp_cost_down[elem.target()]
                j += 1
            my_total_cost[k] = sum(val['cost'] for key, val in my_dict_from_g[k].items())
            my_total_trday[k] = sum(val['trday'] for key, val in my_dict_from_g[k].items()
                                    if val['type'] == 'line')
        return render(request, 'csts/show.html', {
            'port_name_in': port_name_in,
            'port_name_out': port_name_out,
            'm3': m3,
            'my_dict_from_g': my_dict_from_g,
            'my_total_cost': my_total_cost,
            'my_total_trday': my_total_trday,
        })

    else:
        index_form = IndexForm()
    return render(request, 'csts/index.html', {'form': index_form})
