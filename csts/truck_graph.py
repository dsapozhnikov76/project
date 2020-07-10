from graph_tool.all import *


class TruckGraph(graph_tool):

    g = Graph()

    v_prp_id = g.new_vertex_property('string', 'id')
    v_prp_name = g.new_vertex_property('string', 'name')
    v_prp_cost_up = g.new_vertex_property('int', 'cost_in')
    v_prp_cost_down = g.new_vertex_property('int', 'cost_out')
    e_prp_source = g.new_edge_property('string', 'source_port')
    e_prp_target = g.new_edge_property('string', 'target_port')
    e_prp_line = g.new_edge_property('string', 'line')
    e_prp_cost = g.new_edge_property('int', 'cost')

    def __init__(self):
        pass
