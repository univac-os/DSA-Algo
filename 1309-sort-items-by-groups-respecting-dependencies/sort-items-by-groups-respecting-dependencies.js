/**
 * @param {number} n
 * @param {number} m
 * @param {number[]} group
 * @param {number[][]} beforeItems
 * @return {number[]}
 */
var sortItems = function(n, m, group, beforeItems) {
    
        // Grouping then ordering using topological sort
        
        // 1. Give -1 to individual nodes to assign their own groups
        let group_id = m;
        for (let i = 0; i < n; i++) {
            if (group[i] === -1) { // ===
                group[i] = group_id;
                group_id++;
            }
        }

        // 2. Sort all items independently regardless of group dependencies
        let item_g = Array.from({ length: n }, () => []);
        let item_indeg = Array(n).fill(0);

        // 3. Sort all groups regardless of item dependencies
        let group_g = Array.from({ length: group_id }, () => []);
        let group_indeg = Array(group_id).fill(0);

        // 4. Build the connecting graph and calculate in-degrees of items and groups
        for (let curr = 0; curr < n; curr++) {
            for (let bef of beforeItems[curr]) {
                item_g[bef].push(curr);
                item_indeg[curr]++;

                if (group[curr] !== group[bef]) {
                    group_g[group[bef]].push(group[curr]);
                    group_indeg[group[curr]]++;
                }
            }
        }

        // 5. Perform topological sort on items and groups
        function topo(graph, indeg) {
            const visited = [];
            const q = graph
                .map((_, node) => node)
                .filter(node => indeg[node] === 0);
            
            while (q.length > 0) {
                const curr = q.pop();
                visited.push(curr);
                for (const nei of graph[curr]) {
                    indeg[nei]--;
                    if (indeg[nei] === 0) {
                        q.push(nei);
                    }
                }
            }

            return visited.length === graph.length ? visited : [];
        }

        // Calling topological sort
        const item_ord = topo(item_g, item_indeg);
        const group_ord = topo(group_g, group_indeg);

        // 6. Add sorted item_ord to the corresponding group number
        const ord_groups = Array.from({ length: group_id }, () => []);
        for (const item of item_ord) {
            ord_groups[group[item]].push(item);
        }

        // 7. Add sorted group_ord items to the final answer
        const ans = [];
        for (const g_ind of group_ord) {
            ans.push(...ord_groups[g_ind]);
        }

        return ans;
    
};