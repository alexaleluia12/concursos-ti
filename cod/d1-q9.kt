
fun um_f(v: Int) : Boolean {
    if (v % 2 != 0) {
        if (v in 77 .. 81) {
            return true
        }
    }
    
    return false
}

fun main() {
    println(um_f(79))
    println(um_f(78))
    println(um_f(50))
}

