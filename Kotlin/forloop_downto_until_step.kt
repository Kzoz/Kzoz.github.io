fun main() {
    println("-- 1st for loop output --")
    // Write your code below
    for (i in 10 downTo 1){
      println("i= $i")
    }
    
    println("\n-- 2nd for loop output --")
    // Write your code below
    for (j in 1 until 10){
      println("j = $j")
    }
    
    println("\n-- 3rd for loop output --")
    // Write your code below
    for (k in 1..10 step 2){
      println("k = $k")
    }
    
  }