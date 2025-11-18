(module
  (type (;0;) (func (result i32)))
  (type (;1;) (func (param i32) (result i32)))
  (type (;2;) (func))
  (type (;3;) (func (param i32)))
  (func (;0;) (type 2)
    nop)
  (func (;1;) (type 1) (param i32) (result i32)
    (local i32)
    block  ;; label = @1
      local.get 0
      i32.load8_u
      i32.const 98
      i32.ne
      br_if 0 (;@1;)
      local.get 0
      i32.load8_u offset=1
      i32.const 108
      i32.ne
      br_if 0 (;@1;)
      local.get 0
      i32.load8_u offset=2
      i32.const 117
      i32.ne
      br_if 0 (;@1;)
      local.get 0
      i32.load8_u offset=3
      i32.const 101
      i32.ne
      br_if 0 (;@1;)
      local.get 0
      i32.load8_u offset=4
      i32.const 124
      i32.ne
      br_if 0 (;@1;)
      local.get 0
      i32.load8_u offset=5
      i32.const 116
      i32.ne
      br_if 0 (;@1;)
      local.get 0
      i32.load8_u offset=6
      i32.const 117
      i32.ne
      br_if 0 (;@1;)
      local.get 0
      i32.load8_u offset=7
      i32.const 120
      i32.ne
      br_if 0 (;@1;)
      local.get 0
      i32.load8_u offset=8
      i32.const 101
      i32.ne
      br_if 0 (;@1;)
      local.get 0
      i32.load8_u offset=9
      i32.const 100
      i32.ne
      br_if 0 (;@1;)
      local.get 0
      i32.load8_u offset=10
      i32.const 111
      i32.ne
      br_if 0 (;@1;)
      local.get 0
      i32.load8_u offset=11
      i32.const 124
      i32.ne
      br_if 0 (;@1;)
      local.get 0
      i32.load8_u offset=12
      i32.const 100
      i32.ne
      br_if 0 (;@1;)
      local.get 0
      i32.load8_u offset=13
      i32.const 97
      i32.ne
      br_if 0 (;@1;)
      local.get 0
      i32.load8_u offset=14
      i32.const 110
      i32.ne
      br_if 0 (;@1;)
      local.get 0
      i32.load8_u offset=15
      i32.const 99
      i32.ne
      br_if 0 (;@1;)
      local.get 0
      i32.load8_u offset=16
      i32.const 101
      i32.ne
      br_if 0 (;@1;)
      local.get 0
      i32.load8_u offset=17
      i32.const 124
      i32.ne
      br_if 0 (;@1;)
      local.get 0
      i32.load8_u offset=18
      i32.const 99
      i32.ne
      br_if 0 (;@1;)
      local.get 0
      i32.load8_u offset=19
      i32.const 104
      i32.ne
      br_if 0 (;@1;)
      local.get 0
      i32.load8_u offset=20
      i32.const 97
      i32.ne
      br_if 0 (;@1;)
      local.get 0
      i32.load8_u offset=21
      i32.const 111
      i32.ne
      br_if 0 (;@1;)
      local.get 0
      i32.load8_u offset=22
      i32.const 115
      i32.ne
      br_if 0 (;@1;)
      local.get 0
      i32.load8_u offset=23
      i32.const 124
      i32.ne
      br_if 0 (;@1;)
      local.get 0
      i32.load8_u offset=24
      i32.const 112
      i32.ne
      br_if 0 (;@1;)
      local.get 0
      i32.load8_u offset=25
      i32.const 97
      i32.ne
      br_if 0 (;@1;)
      local.get 0
      i32.load8_u offset=26
      i32.const 110
      i32.ne
      br_if 0 (;@1;)
      local.get 0
      i32.load8_u offset=27
      i32.const 99
      i32.ne
      br_if 0 (;@1;)
      local.get 0
      i32.load8_u offset=28
      i32.const 97
      i32.ne
      br_if 0 (;@1;)
      local.get 0
      i32.load8_u offset=29
      i32.const 107
      i32.ne
      br_if 0 (;@1;)
      local.get 0
      i32.load8_u offset=30
      i32.const 101
      i32.ne
      br_if 0 (;@1;)
      local.get 0
      i32.load8_u offset=31
      i32.const 115
      i32.ne
      br_if 0 (;@1;)
      local.get 0
      i32.load8_u offset=32
      i32.eqz
      local.set 1
    end
    local.get 1)
  (func (;2;) (type 0) (result i32)
    i32.const 1040
    i64.const 9038006696380691298
    i64.store
    i32.const 1032
    i64.const 7596551555448135522
    i64.store
    i32.const 1024
    i64.const 3708568498132445812
    i64.store
    i32.const 1048
    i32.const 0
    i32.store8
    i32.const 1024)
  (func (;3;) (type 0) (result i32)
    global.get 0)
  (func (;4;) (type 3) (param i32)
    local.get 0
    global.set 0)
  (func (;5;) (type 1) (param i32) (result i32)
    global.get 0
    local.get 0
    i32.sub
    i32.const -16
    i32.and
    local.tee 0
    global.set 0
    local.get 0)
  (func (;6;) (type 0) (result i32)
    i32.const 1056)
  (table (;0;) 2 2 funcref)
  (memory (;0;) 256 256)
  (global (;0;) (mut i32) (i32.const 5243952))
  (export "memory" (memory 0))
  (export "check" (func 1))
  (export "get_flag" (func 2))
  (export "__indirect_function_table" (table 0))
  (export "_initialize" (func 0))
  (export "__errno_location" (func 6))
  (export "stackSave" (func 3))
  (export "stackRestore" (func 4))
  (export "stackAlloc" (func 5))
  (elem (;0;) (i32.const 1) func 0))
