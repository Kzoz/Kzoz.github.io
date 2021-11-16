fun main() {
    // Write your code below
    grid@ for (i in 1..6) {
      for (j in 'A'..'F') {
        // Write your code below
        if (j == 'C'){
          continue@grid
        }
        
        print("$j$i ")
      }
      println()
    }
  }