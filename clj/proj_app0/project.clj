(defproject proj_app0 "0.1.0-SNAPSHOT"
            :description "FIXME: write description"
            :url "http://example.com/FIXME"
            :license {:name "Eclipse Public License"
                      :url "http://www.eclipse.org/legal/epl-v10.html"}
            :dependencies [[org.clojure/clojure "1.8.0"]
                           [taken "0.1.0"]
                           [proto-repl "0.3.1"]]

            :plugins [[lein-exec "0.3.6"]]
            :main ^:skip-aot proj-app0.core
            :target-path "target/%s"
            :profiles {:uberjar {:aot :all}})
