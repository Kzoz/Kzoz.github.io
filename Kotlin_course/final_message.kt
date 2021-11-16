class Congratulations(val name: String) {

    init {
      println("Dear $name,")
    }
  
    fun message() {
      println("Thank you for embarking on this journey with me. I couldn't have gotten through the treacherous waters of Conditional Creek or hiked up the Looping mountains without your help. You now have the fundamental knowledge to go on and continue your Kotlin journey in the world of android application, web development or more. The world is yours. Good luck! ")
    }
  
    fun signOut() {
      println("With ♥️ , Codey and the Codecademy Team.")
    }
  } 
  
  fun main() {
    println("Please enter your name...")
    var learnerName = readLine()
    var toLearner = Congratulations(learnerName.toString())
    toLearner.message()
    toLearner.signOut()
  }
  /*
  kotlinc Congratulations.kt -include-runtime -d Congratulations.jar
  java -jar Congratulations.jar
   */