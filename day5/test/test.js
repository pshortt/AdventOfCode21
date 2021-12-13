var assert = require('assert');
var day5 = require('../day5');
describe('Part1', function() {
  describe('example', function() {
    it('should return 5', function() {
      assert.equal(day5.solvePart1('example.input'), 5)
    })
  })
})
describe('Part1', function() {
    describe('puzzle', function() {
      it('should return 6189', function() {
        assert.equal(day5.solvePart1('puzzle.input'), 6189)
      })
    })
  })
  describe('Part2', function() {
    describe('example', function() {
      it('should return 12', function() {
        assert.equal(day5.solvePart2('example.input'), 12)
      })
    })
  })
  describe('Part2', function() {
    describe('puzzle', function() {
      it('should return 19164', function() {
        assert.equal(day5.solvePart2('puzzle.input'), 19164)
      })
    })
  })