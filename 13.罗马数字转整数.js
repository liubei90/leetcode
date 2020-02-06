/*
 * @lc app=leetcode.cn id=13 lang=javascript
 *
 * [13] 罗马数字转整数
 */

// @lc code=start
/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    var nummap = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    };
    var pre = null;
    var res = 0;
    for (var i = s.length - 1; i >= 0; i--) {
        var cur = nummap[s.charAt(i)];
        if (!pre) {
            pre = cur;
        }
        res += pre > cur ? (-cur) : cur;
        pre = cur;
    }
    return res;
};
// @lc code=end

[
    'LI',
    'LII',
    'LIII',
    'LIV',
    'LV',
    'LVI',
    'LVII',
    'LVIII',
    'LIX',
    'LX',
].forEach(num => {
    console.log(romanToInt(num));
});