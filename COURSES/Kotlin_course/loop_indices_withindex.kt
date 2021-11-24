fun main() {
    val mySchedule = listOf("Eat Breakfast", "Clean Up", "Work", "Eat Lunch",  "Clean Up", "Work", "Eat Dinner", "Clean Up")
   
    val myTasks = setOf("Eat Breakfast", "Clean Up", "Work", "Eat Lunch",  "Clean Up", "Work", "Eat Dinner", "Clean Up")
  
    println("-- mySchedule Output --")
    // Write your code below
    for (task in mySchedule){
      println(task)
    }
    println("\n-- myTasks Output --")
    // Write your code below
    for ((taskIndex, task) in myTasks.withIndex()){
      println("$taskIndex: $task")
      
    }
    for (tIndex in myTasks.indices){
      println("Indice = $tIndex")
    }
    
  }