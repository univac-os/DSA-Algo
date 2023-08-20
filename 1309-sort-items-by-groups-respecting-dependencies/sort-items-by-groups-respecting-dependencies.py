class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        #grouping then ordering in SORTED so topo sort is needed
        #so we need sort by node in same group and then group by sort and combine both
        #1.give -1 group individual node to group
        group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1

        #2.sort all item regardless of group dependencies
        item_g = [[] for _ in range(n)]
        item_indeg = [0] *n

        #3. sort all groups regardless of item dependencies
        group_g = [[] for _ in range(group_id)]
        group_indeg = [0] *group_id

        #4. make connecting graph and in deg of item and groups separately
        for curr in range(n):
            for bef in beforeItems[curr]:
                item_g[bef].append(curr)
                item_indeg[curr] += 1

                if group[curr] != group[bef]:  # diff group
                    group_g[group[bef]].append(group[curr])
                    group_indeg[group[curr]] += 1

        #5.topo sort on both indivdually kahn algo
        def topo(graph, indeg):
            visited = []
            q=[node for node in range(len(graph)) if indeg[node]==0]
            while q:
                curr = q.pop()
                visited.append(curr)
                for nei in graph[curr]:
                    indeg[nei] -= 1
                    if indeg[nei] == 0:
                        q.append(nei)

            return visited if len(visited) == len(graph) else []

        #calling
        item_ord = topo(item_g, item_indeg)
        group_ord = topo(group_g, group_indeg)

        #6.add sorted item_ord in that group number
        ord_groups = defaultdict(list)
        for item in item_ord:
            ord_groups[group[item]].append(item)

        #7.add sorted group_ord item in sorted
        # Concatenate sorted items in all sorted groups.
        # [group 1, group 2, ... ] -> [(item 1, item 2, ...), (item 1, item 2, ...), ...]
        ans = []
        for g_ind in group_ord:
            ans += ord_groups[g_ind]

        return ans
