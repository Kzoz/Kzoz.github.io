fun main() {
    /*Unlike lists, a set is an un-ordered collection, thus we can’t use 
    square brackets and indices to retrieve its elements. However, a set 
    is an intelligent tool that stores its elements in the order in which 
    each element was inserted. We can utilize this order along with a function, 
    elementAt(), to access and retrieve elements.
    The elementAt() function accepts an Integer value and returns the element 
    at that position. This function is useful for collections that do not 
    possess index access. */ 
    var islandsOfHawaii = setOf("Maui","Lanai","Oahu","Kauai")
    println(islandsOfHawaii.elementAt(2))
    println(islandsOfHawaii.elementAtOrNull(6))
  }