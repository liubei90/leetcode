/*
 * @lc app=leetcode.cn id=14 lang=javascript
 *
 * [14] 最长公共前缀
 */

// @lc code=start
/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    var res = '';
    // var curChar = null;
    var index = 0;
    _label: while (true) {
        var curChar = strs[0] && strs[0][index];
        if (!curChar) break;
        for (var i = 0; i < strs.length; i++) {
            if (curChar !== strs[i][index]) break _label;
        }
        res += curChar;
        index++;
    }
    return res;
};
// @lc code=end

