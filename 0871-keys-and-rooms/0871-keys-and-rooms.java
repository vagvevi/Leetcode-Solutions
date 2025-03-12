class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        Set<Integer> visited = new HashSet<>();
        Queue<Integer> queue = new LinkedList<>();
        visited.add(0);
        queue.add(0);
        while(!queue.isEmpty()){
            int room = queue.poll();
            for(int key : rooms.get(room)){
                if(!visited.contains(key)){
                    visited.add(key);
                    queue.add(key);
                }
            }
        }
        return visited.size() == rooms.size();
    }
}