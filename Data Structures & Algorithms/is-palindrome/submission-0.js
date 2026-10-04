class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let testString = s.toLowerCase().replaceAll(/[^a-zA-Z0-9]/g, '');
        let left = 0;
        let right = testString.length - 1;

        while(left < right)
        {
            if(testString[left] !== testString[right])
            {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
