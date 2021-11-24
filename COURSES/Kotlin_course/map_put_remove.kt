fun main() {
    // Write your code below 🖼
  
    var momaPaintings = mutableMapOf("Les Demoiselles d'avignon" to "Pablo Picasso", "The Starry Night" to "Vincent Van Gogh", "Mona Lisa" to "Leonardo Da Vinci", "The Persistance of Memory" to "Salvador Dali")
  
    if (!momaPaintings.containsValue("Claude Monet")) {
      // Write your code for Step 1 here 
      momaPaintings.put("Water Lillies", "Claude Monet")
    }
      momaPaintings.remove("Mona Lisa")
      // Write your code for Step 2 here
      println(momaPaintings)
    
  
  }