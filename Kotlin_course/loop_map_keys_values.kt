fun main(){
    val myClothes = mapOf("Shirts" to 7, "Pairs of Pants" to 4, "Jackets" to 2)
    println("KEYS")
    for (itemName in myClothes.keys) {
        println(itemName)
    }

    println("\nVALUES")
    for (itemCount in myClothes.values) {
        println(itemCount)
    }
}