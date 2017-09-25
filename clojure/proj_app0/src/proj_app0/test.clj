(println
 (+ 1 2 3 4 5)

 (+ 1 (* 2 3) 4))

(println
 (+ 1 2 3 4))

(println
 (+ 1 (|* |2 3) 4))

(println
 (+ 1 2 3))

(str "It was the panda " "in the library " "with a dust buster")

(if false
  (println "true")
  (println "false"))

(def true_false
  (if true
    (println "true")
    (println "false")))

(def true_false
  (if false
    (do (println "Success!")
        "By Zeus's hammer!")
    (do (println "Failure!")
        "By Aquaman's trident!")))
