class Person(val name: String, val age: Int, val favoriteColor: String)

fun main() {
  // Create your instances below 
val me = Person("MS",5,"grey")
val myFriend = Person("MK",5,"orange")
println("${me.name} is ${me.age} years old and my favorite color is ${me.favoriteColor}.")
println("${myFriend.name} is ${myFriend.age} years old and their favorite color is ${myFriend.favoriteColor}.")

}