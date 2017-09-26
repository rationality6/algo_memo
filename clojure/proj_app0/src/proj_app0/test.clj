(str "It was the panda " "in the library " "with a dust buster")

(def foo "foobar")

(if false
  (println "true")
  (println "false"))

(if (or "true" "false"))
(if false ("false") "true")

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

(defn foobar [name]
  (println ()))

(for [n [1 2 3 4 5]](* 2 n))
(for [n [2 2 3]](+ 4 n))
(for [n [1 2 3]](Math/pow n 2))

(def looping
  (for [n [1 2 3 4 5]]
    (n)))


(range 3 8)


(->>
  (range 1000)
  (filter (fn [x] (or (= (mod x 3) 0) (= (mod x 5) 0))))
  (reduce +)
  println)
