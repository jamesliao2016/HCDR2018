class twoSumSolution {
  def twoSum(nums: Array[Int], target: Int): Array[Int]={
    val nums_map = scala.collection.mutable.hashMap[Int,Int]()
    var result: Array(Int) = Array(0,0)
    var i = 0
    while (result.sum==0) {
      val complement = target - nums(i)
      if (nums_map.contains(complement)){
        result(0) = i
        result(1) = nums_map(complement)
      }
      else{
        nums_map(complement) = i
      }
      i += 1
    }
    result
  }

}
