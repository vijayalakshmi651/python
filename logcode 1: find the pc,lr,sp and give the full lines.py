logcode='''[  153.627416] Unable to handle kernel NULL pointer dereference at virtual address 0000000000000008
[  153.627431] Mem abort info:
[  153.627435]   ESR = 0x96000004
[  153.627439]   EC = 0x25: DABT (current EL), IL = 32 bits
[  153.627444]   SET = 0, FnV = 0
[  153.627447]   EA = 0, S1PTW = 0
[  153.627451] Data abort info:
[  153.627454]   ISV = 0, ISS = 0x00000004
[  153.627458]   CM = 0, WnR = 0
[  153.627463] user pgtable: 4k pages, 48-bit VAs, pgdp=0000000081cdb000
[  153.627471] [0000000000000008] pgd=0000000000000000
[  153.627479] Internal error: Oops: 96000004 [#1] SMP
[  153.627484] Modules linked in: my_driver_module bluetooth e1000e
[  153.627491] CPU: 2 PID: 1348 Comm: my_custom_task Tainted: G        W        5.10.0-14-generic #1
[  153.627498] Hardware name: ARM Juno development board
[  153.627503] pstate: 80000005 (Nzcv daif -PAN -UAO -TCO BTYPE=--)
[  153.627510] pc : my_driver_probe+0x34/0x80 [my_driver_module]
[  153.627516] lr : platform_probe+0x20/0x50
[  153.627521] sp : ffff8000136c3c20
[  153.627525] x29: ffff8000136c3c20 x28: ffff00001104c000
[  153.627532] x27: ffff000011045000 x26: 0000000000000000
[  153.627539] x25: ffff0000110471d0 x24: ffff000011047180
[  153.627545] x23: ffff000011045800 x22: ffff0000110457c8
[  153.627551] x21: ffff000011045100 x20: 0000000000000000
[  153.627558] x19: ffff000011045000 x18: 0000000000000000
[  153.627564] x17: 0000000000000000 x16: 0000000000000000
[  153.627571] x15: 0000000000000000 x14: 0000000000000000
[  153.627577] x13: 0000000000000000 x12: 0000000000000000
[  153.627584] x11: 0000000000000000 x10: 0000000000000000
[  153.627590] x9 : 0000000000000000 x8 : 0000000000000000
[  153.627596] x7 : 0000000000000000 x6 : 0000000000000000
[  153.627602] x5 : 0000000000000000 x4 : 0000000000000000
[  153.627609] x3 : 0000000000000000 x2 : 0000000000000000
[  153.627615] x1 : 0000000000000008 x0 : ffff000011045000
[  153.627623] Call trace:
[  153.627627]  my_driver_probe+0x34/0x80 [my_driver_module]
[  153.627633]  platform_probe+0x20/0x50
[  153.627638]  really_probe+0xd4/0x3e0
[  153.627643]  __driver_probe_device+0x84/0x140
[  153.627649]  driver_probe_device+0x34/0x110
[  153.627655]  __device_attach_driver+0x8c/0x120
[  153.627660]  bus_for_each_drv+0x60/0xa0
[  153.627666]  __device_attach+0xd0/0x150
[  153.627672]  device_initial_probe+0x14/0x20
[  153.627678]  bus_probe_device+0x90/0xa0
[  153.627683]  device_add+0x408/0x620
[  153.627688]  platform_device_add+0x13c/0x2c0
[  153.627694]  platform_device_register_full+0x84/0x100
[  153.627701]  platform_device_register+0x24/0x40
[  153.627707]  my_driver_init+0x20/0x100 [my_driver_module]
[  153.627714]  do_one_initcall+0x44/0x1c0
[  153.627719]  do_init_module+0x54/0x200
[  153.627724]  load_module+0x22c4/0x29d0
[  153.627729]  __do_sys_finit_module+0xbc/0xf0
[  153.627735]  __arm64_sys_finit_module+0x24/0x30
[  153.627741]  invoke_syscall+0x44/0x100
[  153.627746]  el0_svc_common.constprop.0+0x44/0xe0
[  153.627752]  do_el0_svc+0x18/0x50
[  153.627758]  el0_svc+0x1c/0x50
[  153.627763]  el0t_64_sync_handler+0xf0/0x120
[  153.627768]  el0t_64_sync+0x190/0x194
[  153.627773] Code: f94260 b40000c0 f9400000 f9001bf5 (f9400001)
[  153.627782] ---[ end trace 1f9a2c6fd0135467 ]---
[  153.627787] Kernel panic - not syncing: Fatal exception in interrupt
[  153.627794] SMP: stopping secondary CPUs
[  153.628012] Kernel Offset: 0x284e0000 from 0xffffffc010000000
[  153.628020] CPU features: 0x00000006,21006004
[  153.628026] Memory Limit: none'''

log_list = logcode.splitlines()
#print(log_list)
str1="pc"
str2="lr"
str3="sp"
dict={}
for i in log_list:
    if str1 in i:
        dict["pc"]=i
    elif str2 in i:
        dict["lr"]=i
    elif str3 in i:
       dict["sp"]=i
        
print(dict)
    
        
