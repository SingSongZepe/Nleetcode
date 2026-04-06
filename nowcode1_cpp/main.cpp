#include <iostream>
#include <memory>
#include <string.h>
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    typedef long long LL;
    vector<string> GetSpaceUsageMaxDir(string queryDir, vector<string>& filePathList, vector<long>& fileSizeList) {
        // write code here
        int n = queryDir.size();

        std::unordered_map<string, LL> subDir;
        for (int i = 0; i < filePathList.size(); i++) {
            const string& subPath = filePathList[i];
            if (subPath.substr(0, n) == queryDir) { // same prefix
                // find the first '/' after n
                int first_idx = subPath.size();
                for (int j = n; j < subPath.size(); j++) {
                    if (subPath[j] == '/') {
                        first_idx = j;
                        break;
                    }
                }
                string subPathName = subPath.substr(n+1, first_idx-n-2);
                subDir[subPathName] += fileSizeList[i];
            }
        }

        // traverse the hashmap to find the max subpath
        auto subDirCurr = subDir.begin();
        int maxSize = 0;
        vector<string> maxSizeSubPathNames;
        while (subDirCurr != subDir.end()) {
            if (subDirCurr->second > maxSize) {
                maxSize = subDirCurr->second;
                maxSizeSubPathNames.clear();
                maxSizeSubPathNames.emplace_back(subDirCurr->first);
            } else if (subDirCurr->second == maxSize) {
                maxSizeSubPathNames.emplace_back(subDirCurr->first);
            }
            subDirCurr++;
        }

        vector<string> result;
        for (int i = 0; i < maxSizeSubPathNames.size(); i++) {
            result.emplace_back(queryDir + '/' + maxSizeSubPathNames[i]);
        }
        
        return result;
    }
};

// return true 
// iff a start with b
bool start_with(const string& a, const string& b) {
    if (a.size() < b.size()) return false;
    for (int i = 0; i < b.size(); i++) {
        if (a[i] != b[i]) return false;
    }
    return true;
}

// the first sub_name after n
// n should be a '/' in @param a
string sub_name(const string& a, int n) {
    // find the next '/'
    int first_idx = a.size();
    for (int i = n+1; i < a.size(); i++) {
        if (a[i] == '/') {
            first_idx = i;
            break;
        }
    }
    return a.substr(n, first_idx-n);
}

// #define DBUG

class Solution1 {
public:
    typedef long long LL;
    
    vector<string> GetSpaceUsageMaxDir(string queryDir, vector<string>& filePathList, vector<long>& fileSizeList) {
        int n = queryDir.size();
        std::unordered_map<string, LL> map;

        for (int i = 0; i < filePathList.size(); i++) {
            const auto& filePath = filePathList[i];

            if (start_with(filePath, queryDir)) {
#ifdef DBUG
                std::cout << filePath << " start with " << queryDir << std::endl;
#endif
                // filePath is file under queryDir
                // find the dir name or file name
                
                string subPathName = sub_name(filePath, n);
#ifdef DBUG
                std::cout << "find sub path name <" << subPathName << "> of " << filePath << std::endl;           
#endif
                map[subPathName] += fileSizeList[i];
            }
        }

        int maxSize = 0;
        vector<string> maxSubNames;
        auto curr = map.begin();
        while (curr != map.end()) {
            if (curr->second > maxSize) {
                maxSize = curr->second;
                maxSubNames.clear();
                maxSubNames.emplace_back(curr->first);
            } else if (curr->second == maxSize) {
                maxSubNames.emplace_back(curr->first);
            }

#ifdef DBUG    
            std::cout << curr->first << " has " << curr->second << std::endl;
#endif
            curr++;
        }

        vector<string> result;
        for (const auto& subName : maxSubNames) {
            result.emplace_back(queryDir + subName);
#ifdef DBUG
            std::cout << "subname " << subName << std::endl;       
#endif
        }

        std::sort(result.begin(), result.end());
        return result;
    }
};

void test() {
    string a = "/dir1/dir2/file1";
    string b = "/dir1";

    std::cout << sub_name(a, b.size()) << std::endl;
}

int main() {
    // test();

    // return 0;
    string a = "/dir1/dir2-1";
    vector<string> b = {
        "/dir0/dir1-1/file1-1",
        "/dir1/dir1-1/file1-1",
        "/dir1/dir2-1/file3-1",
        "/dir1/dir2-1/file3-2",
        "/dir1/dir2-1/dir3-1/file4-1"
    };
    vector<long> c = {
        8192, 81920, 2048, 8192, 1024
    };
    vector<string> result;

    // auto sol = make_unique<Solution>();
    // result = sol->GetSpaceUsageMaxDir(a, b, c);

    // for (const auto& s : result) {
    //     std::cout << s << "\n";
    // }

    // std::cout << "\n";

    a = "/dir1";
    b = {"/dir1/dir1/file1","/dir1/dir1/file2","/dir1/dir2/file3"};
    c = {1024,2048,3072};

    auto sol1 = make_unique<Solution1>();
    result = sol1->GetSpaceUsageMaxDir(a, b, c);

    for (const auto& s : result) {
        std::cout << s << "\n";
    }

    return 0;
}
