const fs = require('fs')

module.exports= {
    solvePart1: function (fname){
        return solve(fname, true)       
    },
    solvePart2: function (fname){
        return solve(fname)       
    }
}
// helper functions
function solve(fname, part1=false){
    let content = fs.readFileSync(fname).toString()
    const itxMap = new Map() // keys: all points plotted; ele: how many lines are plotted on the given point
    allPoints(content, part1).forEach( // context list contains each point plotted incl duplicates    
        p => itxMap.set(p, (itxMap.get(p) ?? 0) + 1)) 
    return [...itxMap.keys()].reduce((p, c) => 
            (itxMap.get(c) > 1 ?  p + 1 : p)
            , 0)
}
const allPoints = function(content, part1=false){
    var lines = content.split('\r\n') // get list of all 'line' objects being plotted
                        .map(s => s.split(' -> '))
                        .map(startToEnd => new line(startToEnd))
                        .filter((part1 ? l => (l.isHorizontal() || l.isVertical()) : () => true))                      
    return lines.map(l => l.points()) // expand list of line object to list of all points being plotted
                .reduce((p, c) => p.concat(c), [])
}
const reduceFraction = function (n,d){
    var gcd = function gcd(a,b){
      return b ? gcd(b, a%b) : a
    }
    gcd = gcd(Math.abs(n),Math.abs(d))  // always preserve negative sign
    var result = [n/gcd, d/gcd]
    return result
}
// helper classes
class line {
    constructor(startToEnd) {
        var result = startToEnd.map(p_str => new point(p_str));
        this.start = result[0];
        this.end = result[1];
        [this.yStep, this.xStep] = reduceFraction(this.end.y - this.start.y, this.end.x - this.start.x)
    }
    isVertical(){ return this.start.x === this.end.x }
    isHorizontal(){ return this.start.y === this.end.y }
    points(){ // needs refactor
        var xi = this.start.x
        var yi = this.start.y
        var result = []
        do{
            result.push(xi + ',' + yi)
            xi = (xi != this.end.x ? xi + this.xStep: xi)
            yi = (yi != this.end.y ? yi + this.yStep: yi)
        }while (xi != this.end.x || yi != this.end.y)
        result.push(xi + ',' + yi)       
        return result
    }
}
class point {
    constructor(point_str) {
        var point_arr = point_str.split(',').map(s => parseInt(s));
        this.x = point_arr[0];
        this.y = point_arr[1];
    }
}
