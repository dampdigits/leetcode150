class RandomizedSet {
    private ArrayList<Integer> vals;
    private Map<Integer, Integer> idx;

    public RandomizedSet() {
        vals = new ArrayList<>();
        idx = new HashMap<>();
    }
    
    public boolean insert(int val) {
        if (idx.containsKey(val)) return false;

        vals.add(val);
        idx.put(val, vals.size() -1);
        return true;
    }
    
    public boolean remove(int val) {
        if (! idx.containsKey(val)) return false;

        int index = idx.get(val);
        vals.set(index, vals.get(vals.size() -1));
        idx.put(vals.get(index), index);
        vals.remove(vals.size() -1);
        idx.remove(val);

        return true;
    }
    
    public int getRandom() {
        Random rand = new Random();
        return vals.get(rand.nextInt(vals.size()));
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
