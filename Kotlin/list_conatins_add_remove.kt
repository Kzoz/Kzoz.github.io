fun main() {

    val planets = mutableListOf("Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto")
  
    // Write your code below 🪐
    planets.remove("Pluto")
    planets.add("Earth")
    println(planets.random())
    println(planets.contains("Jupiter"))
  
  }