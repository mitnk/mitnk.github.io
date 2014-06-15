    :::scheme
    ; Votes divided by the age in hours to the gravityth power.
    ; Would be interesting to scale gravity in a slider.
     
    (= gravity* 1.8 timebase* 120 front-threshold* 1
       nourl-factor* .4 lightweight-factor* .3 )
     
    (def frontpage-rank (s (o scorefn realscore) (o gravity gravity*))
      (* (/ (let base (- (scorefn s) 1)
              (if (> base 0) (expt base .8) base))
            (expt (/ (+ (item-age s) timebase*) 60) gravity))
         (if (no (in s!type 'story 'poll))  1
             (blank s!url)                  nourl-factor*
             (lightweight s)                (min lightweight-factor*
                                                 (contro-factor s))
                                            (contro-factor s))))

Source: [ruanyifeng.com](http://www.ruanyifeng.com/blog/2012/02/ranking_algorithm_hacker_news.html)

    :::scheme
    (= gravity* 1.8 timebase* 120 front-threshold* 1
       nourl-factor* .4 lightweight-factor* .17 gag-factor* .1)

    (def frontpage-rank (s (o scorefn realscore) (o gravity gravity*))
      (* (/ (let base (- (scorefn s) 1)
              (if (> base 0) (expt base .8) base))
            (expt (/ (+ (item-age s) timebase*) 60) gravity))
         (if (no (in s!type 'story 'poll))  .8
             (blank s!url)                  nourl-factor*
             (mem 'bury s!keys)             .001
                                            (* (contro-factor s)
                                               (if (mem 'gag s!keys)
                                                    gag-factor*
                                                   (lightweight s)
                                                    lightweight-factor*
                                                   1)))))

From: [amix.dk](http://amix.dk/blog/post/19574)
Ref: [HackerNews](http://news.ycombinator.com/item?id=1781013)