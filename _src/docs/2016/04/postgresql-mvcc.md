PostgreSQL MVCC 简介
===================

当多个进程读写同一table时 PostgreSQL 用 MVCC 来维持数据一致。
VMCC，即 Multiple Version Concurrency Control，并非
PostgreSQL 专有；它是 DBMS 都会用到的技术。

## 为什么需要 MVCC ？

如果进程A在读数据库里的数据时，另一进程B同时
对同一数据进行写入时，进程A可能读到B写了一半的数据，
即坏数据。


