fun main() {
    var sHU = 17000
    var pungency: String
  
    // Write your code below
    when (sHU) {
      in 0..699 -> pungency = "very mild"
      in 700..2999 -> pungency = "mild"
      in 3000..24999 -> pungency = "moderate"
      in 25000..69999 -> pungency = "high"
      else -> pungency = "very high"
    }
    println(pungency)
    
   
  
  }