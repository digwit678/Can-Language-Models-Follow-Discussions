import pickle
import igraph as ig

pickle_file = open(r"C:\Users\nico\Dropbox\HSLU\Bachelorarbeit\Code\data\dumped_discussions_first.pickle", "rb")
# load discussions
# dumped_discussions = pickle.load(open(pickle_file, "rb"))
dumped_discussions = pickle.load(pickle_file)


# parse_graph
def parse_discussion_graph(discussion):
    discussion_graph = ig.Graph()

    vertex_id_mappings = {}

    for i, claim in enumerate(discussion["discussion"]["claims"]):
        vertex = discussion_graph.add_vertex({
            "id": claim["id"],
            "text": claim["text"]
        })
        vertex_id_mappings[claim["id"]] = vertex.index

    for location in discussion["discussion"]["locations"]:

        if location["isDeleted"] == True:
            continue

        if location["parentId"] is None:
            continue

        source = vertex_id_mappings[location["targetId"]]
        parent = vertex_id_mappings[location["parentId"]]

        discussion_graph.add_edge(
            source=source, target=parent, relation=location["relation"]
        )

    ## ignore isolated (no edge) claims
    discussion_graph.vs.select(_degree=0).delete()

    return discussion_graph


parsed_discussion_graphs = [
    parse_discussion_graph(dumped_discussion)
    for dumped_discussion in dumped_discussions
]
