import os
import pkg_resources

def calc_container(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def calc_installed_sizes():
    dists = [d for d in pkg_resources.working_set]

    total_size = 0
    print (f"Size of Dependencies")
    print("-"*40)
    for dist in dists:
        # ignore pre-installed pip and setuptools
        if dist.project_name in ["pip", "setuptools"]:
            continue
        try:
            path = os.path.join(dist.location, dist.project_name)
            size = calc_container(path)
            total_size += size
            if size/1000 > 1.0:
                print (f"{dist}: {size/1000} KB")
                print("-"*40)
        except OSError:
            '{} no longer exists'.format(dist.project_name)

    print (f"Total Size (including dependencies): {total_size/1000} KB")
    print (f"Total Size (including dependencies): {total_size/(1000 * 1024)} MB")

if __name__ == "__main__":
    calc_installed_sizes()