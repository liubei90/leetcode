/*
 * @lc app=leetcode.cn id=7 lang=javascript
 *
 * [7] 整数反转
 */

// @lc code=start
/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    
};
// @lc code=end

var data = {
    '123': '321',
    '-123': '-321',
    '120': '21'
}
Object.keys(data).forEach(key => {
    var num = Number(key);
    var res = String(reverse(num));
    if (res !== data[key]) {
        console.log('error', key, res);
    } else {
        console.log('success', key, res);
    }
});