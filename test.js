"""js课堂笔记"""
d = '100'
let b = "abcabc"
c = `test string
    ${d + b}  
    1234
`
// {}里面放的是表达式
console.log(c)
console.log(b.charAt(2))
console.log(b[2])
b[0] = 'e'
console.log(b)  // abc,并没有改变，与python是一样的
console.log(b.concat('def'))
console.log(b.replace('bc', 'efg'))  // 不论怎么替换，原字符串不会改变
console.log(b.search('b'))  // 返回字符对应的索引1

console.log(b.substr(1, 3))  // 前包后也包，记不住就测试
console.log(b.substring(1, 3))  // 前包后不包

console.log(b.slice(1, 3))

let i = 0
let a = i++
console.log(a, i)
console.log(a, i++)
console.log(a, ++i)

a = -i++
console.log(a, i++)
console.log(a, ++i)
 

console.log(1000 > '10a')  // 隐式类型转换仍然无法比较大小，所以直接返回fasle

m = 100, 5  // 注意js中没有元组，逗号的优先级最低
// m = 100, 5  // python中的逗号优先级要高于赋值
