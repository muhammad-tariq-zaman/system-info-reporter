import platform, os
def info():
    mem_total = None
    try:
        for line in open("/proc/meminfo"):
            if line.startswith("MemTotal:"):
                mem_total = int(line.split()[1]) // 1024; break
    except OSError: pass
    return {"os": platform.system(), "release": platform.release(), "machine": platform.machine(),
            "python": platform.python_version(), "cpu_count": os.cpu_count(), "mem_total_mb": mem_total}
if __name__ == "__main__":
    for k, v in info().items(): print(f"{k}: {v}")
