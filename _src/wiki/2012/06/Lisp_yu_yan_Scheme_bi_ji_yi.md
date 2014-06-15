复合过程

    :::scheme
    #lang racket

    ; run it with "racket xxx.scm"
    ; the outputs are:
    ; 49
    ; 25
    ; #f

    (define (square x)
        (* x x))

    (define (sum-of-squares x y)
        (+ (square x) (square y)))

    (square 7)
    (sum-of-squares 3 4)

    (define x 100)
    (< x 99)


条件表达式

    :::scheme
    (define (abs1 x)
      (cond ((> x 0) x)
            ((= x 0) 0)
            ((< x 0) (- x))))

    (define (abs2 x)
      (cond ((< x 0) (- x))
            (else x)))

    (define (abs3 x)
      (if (< x 0)
          (- x)
          x))


运算符为复合表达式

    :::scheme
    (define (a-plus-abs-b a b)
        ((if (< b 0) - +) a b)

    (a-plus-abs-b 4 3) ; => 7
    (a-plus-abs-b 4 -3) ; => 7



谓词

    :::scheme
    ; the outputs are:
    ; #t
    ; #f
    ; #t
    ; #t

    (define (between n x y)
        (and (> n x) (< x y)))

    (define (=> x y)
        (or (> x y) (= x y)))

    (define (=< x y)
        (not (> x y)))

    (between 7 5 10)
    (=> 7 8)
    (=< 7 8)
    (and (> 1 0) (> 2 0) (> 3 0))

牛顿法：

    :::scheme
    ; 牛顿法求平方根
    ; 如果对x的平方根的值有了一个猜测y，
    ; 那么通过一个简单操作可以得到一个更好的猜测：
    ; 只需要求出 y 和 x/y 的平均值

    (define (diff y x)
        (abs (- (* y y) x)))

    (define (improve y x)
        (/ (+ y (/ x y)) 2))

    (define (good-enough? y x)
        (< (diff y x) 0.00001))

    (define (sqrt-iter guess x)
        (if (good-enough? guess x)
            guess
            (sqrt-iter (improve guess x) x)))

    (define (sqrt2 x)
        (sqrt-iter 1.0 x))

    (sqrt2 2)


当开方数值非常小或非常大时，如 `0.123e-7` 或 `2e30`，上面检测good-enough时就不好使了，更好的办法是检测猜测数值变化的比率。

    :::scheme
    ; 牛顿法求平方根 （改进版）
    ; 如果对x的平方根的值有了一个猜测y，
    ; 那么通过一个简单操作可以得到一个更好的猜测：
    ; 只需要求出 y 和 x/y 的平均值
    ; sqrt() is a BIF (Built-in Function)

    (define (grow-rate y x)
        (abs (/ (- (* y y) x) x)))

    (define (improve y x)
        (/ (+ y (/ x y)) 2))

    (define (good-enough? y x)
        (< (grow-rate y x) 0.00001))

    (define (sqrt-iter guess x)
        (if (good-enough? guess x)
            guess
            (sqrt-iter (improve guess x) x)))

    (define (sqrt2 x)
        (sqrt-iter 1.0 x))


    (sqrt2 2e30)
    (sqrt 2e30)
    (sqrt2 1.23e-7)
    (sqrt 1.23e-7)


为了解决潜在的命令空间污染问题，可以用**块结构**将函数重写

    :::scheme
    (define (sqrt2 x)
        (define (sqrt-iter guess)
            (if (good-enough? guess)
                guess
                (sqrt-iter (improve guess))))
        (define (good-enough? guess)
            (< (abs (- (/ (* guess guess) x) 1)) 0.00001))
        (define (improve y)
            (/ (+ (/ x y) y) 2))
        (sqrt-iter 1.0))

注意，在这个函数里我们省略了 `sqrt-iter`, `good-enough?`, 和 `improve`的形参中的x，因为在这些过程中可以直接用由`sqrt2`传入的自由变量x
