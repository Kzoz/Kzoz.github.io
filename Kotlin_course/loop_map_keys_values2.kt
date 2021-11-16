fun main(){
    val myClothes = mapOf("Shirts" to 7, "Pairs of Pants" to 4, "Jackets" to 2)
    for (itemEntry in myClothes) {
        println("I have ${itemEntry.value} ${itemEntry.key}")
    }
}
fun main(){
    val favoriteColors = mapOf("Jesse" to "Violet", "Megan" to "Red", "Tamala" to "Blue", "Jordan" to "Pink")
  
    println("\n-- Key: Value Output --")
    // Write your code below
    for (favoriteEntry in favoriteColors){
        println("${favoriteEntry.key}: ${favoriteEntry.value}")
    }
    
    println("\n-- Only Values Output --")
    // Write your code below
    for (color in favoriteColors.values){
        println(color)
    }
}