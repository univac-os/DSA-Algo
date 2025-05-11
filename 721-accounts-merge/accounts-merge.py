class Solution:
    def accountsMerge(self,accounts):
        # Build the graph
        email_to_name = {}
        graph = {}
        
        for account in accounts:
            name = account[0]
            # Connect all emails in this account with each other
            for email in account[1:]:
                if email not in graph:
                    graph[email] = set()
                email_to_name[email] = name
                
                # Connect this email with all other emails in this account
                for other_email in account[1:]:
                    if email != other_email:
                        graph[email].add(other_email)
                        if other_email not in graph:
                            graph[other_email] = set()
                        graph[other_email].add(email)
        
        # DFS function
        def dfs(email, component, visited):
            visited.add(email)
            component.append(email)
            
            for neighbor in graph[email]:
                if neighbor not in visited:
                    dfs(neighbor, component, visited)
        
        # Find connected components
        visited = set()
        result = []
        
        for email in graph:
            if email not in visited:
                component = []
                dfs(email, component, visited)
                component.sort()  # Sort emails alphabetically
                result.append([email_to_name[email]] + component)
        
        return result