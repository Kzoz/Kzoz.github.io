fun main() {
    // Write your code below 📝
    //variable.first()
    //variable.last()
    val testGrades = mutableSetOf<Int>(65,50,72,80,53,84)
    var sum = testGrades.sum()
    var numStudents =testGrades.size
    var average = sum / numStudents
    when (average){
      in 0..65 -> println("Failed")
      else -> println("Passed") 
    }
  
  
  }