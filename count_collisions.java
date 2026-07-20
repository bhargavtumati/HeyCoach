/*Traffic Rush
You're a traffic engineer stuck in a rush hour nightmare on an infinitely long highway. But it's not your typical gridlock – this road has only cars moving in either direction (left or right) or simply stalled out! Your job is to predict the chaos: how many collisions will occur before the dust settles?

Given a string direction (length <= 10^5) where each character is 'L' (left), 'R' (right), or 'S' (stopped), predict the total number of collisions that will happen on the road. Collisions occur when:

Two moving cars (one left, one right) meet – a head-on smash! Increases collisions by 2. A moving car slams into a stopped car – rear-end ouch! Increases collisions by 1. Remember, once a car collides, it stops and becomes an obstacle for future crashes. Cars never change direction or speed.

Example 1:
Scenario: "RLRSLL"

Collisions: 5 (2 for cars 0/1, 1 for cars 2/3, 1 for cars 3/4, 1 for cars 4/5)
Example 2:
Scenario: "LLRR"

Collisions: 0 (no head-on or rear-end collisions)
Input:
A single line containing the string directions, where each character can be:
'L': denotes a car moving left.
'R': denotes a car moving right.
'S': denotes a car staying stationary.
Output:
A single integer representing the total number of collisions that will occur on the road.
Constraints:
The length of directions (n) must be between 1 and 10^5 (inclusive).
Each character in directions must be either 'L', 'R', or 'S'.*/

class CountCollisions {

    public int countCollisions(String dirs) {
        int coll = 0;

        if (dirs.length() <= 1) {
            return coll;
        }

        for (int i = 0; i < dirs.length() - 1; i++) {

            if (dirs.charAt(i) == dirs.charAt(i + 1)
                    && dirs.charAt(i) != 'S'
                    && coll == 0) {
                i++;
            } else if (((dirs.charAt(i) == 'R' && dirs.charAt(i + 1) == 'L')
                    || (dirs.charAt(i) == 'L' && dirs.charAt(i + 1) == 'R'))
                    && coll == 0) {
                coll += 2;
                i++;
            } else {
                coll++;
            }
        }

        return coll;
    }

    public static void main(String[] args) {
        CountCollisions obj = new CountCollisions();
        System.out.println(obj.countCollisions("RLRSLL"));
    }
}