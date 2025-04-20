class Solution:
    def _build_adjacency_matrix(
        self, prerequisites: list[list[int]], num_courses
    ) -> dict:
        adjacency_matrix = {i: [] for i in range(num_courses)}
        for dest, source in prerequisites:
            adjacency_matrix[source].append(dest)
        return adjacency_matrix

    def _dfs(self, course: int, adjacency_matrix: dict, visited: set, numCourses: int):
        if course in visited:
            return False

        if adjacency_matrix[course] == []:
            return True

        visited.add(course)

        for pre in adjacency_matrix[course]:
            if not self._dfs(pre, adjacency_matrix, visited, numCourses):
                return False

        visited.remove(course)

        # I need this cause first I get into a node, and recursively traverse it's depedencies.
        # When i get to the last one (in terms of depth) I return True cause has no dependencies.
        # After that, if i return true and im done with the cycle, it means that nothing returned false, so all the dependencies
        # of course are doable, so i can set the current node dependencies to None.
        # Doing so will backpropagate the true value.
        adjacency_matrix[course] = []

        return True

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adjacency_matrix = self._build_adjacency_matrix(prerequisites, numCourses)
        visited = set()

        for course in range(numCourses):
            if not self._dfs(course, adjacency_matrix, visited, numCourses):
                return False

        return True
