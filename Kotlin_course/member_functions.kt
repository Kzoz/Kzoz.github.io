class Dog(val name: String, val breed: String, val competitionsParticipated: List<String>) {
  
    init {
      for (comp in competitionsParticipated) {
        println("$name participated in $comp.")
      }
    }
  
    // Write your function below 
  fun speak(){
    println("$name says: Wooof!")
  }
  
  }
  
  fun main() {
    // Write your instance below 🐩
  val maxie = Dog("Maxie","Poodle",listOf("Westminster Kennel Club Dog Show","AKC"))
  maxie.speak()
  }