#include <iostream>
#include <vector>
using namespace std;

// A utility structure to represent a tile or a missing position
struct Tile {
    int type, x, y;
    Tile(int type, int x, int y) : type(type), x(x), y(y) {}
};

vector<Tile> answer;

void tiling(int x1, int x2, int y1, int y2, pair<int, int> missing) {
    // Base case: If the current tile is 1x1
    if ((x2 - x1 == 1) && (y2 - y1 == 1)) {
        int tile_mapping[2][2] = {{0, 1}, {2, 3}};
        answer.push_back(Tile(tile_mapping[missing.first - x1][missing.second - y1], x1, y1));
        return;
    }
    // Determine the midpoint
    int mid_x = (x1 + x2) / 2;
    int mid_y = (y1 + y2) / 2;
    int X = missing.first;
    int Y = missing.second;
    // Determine which quadrant the missing tile is in and recurse appropriately
    if (X < mid_x && Y < mid_y) { // Q1
        answer.push_back(Tile(0, mid_x, mid_y));
        tiling(x1, mid_x, y1, mid_y, missing);
    } else if (X >= mid_x && Y < mid_y) { // Q2
        answer.push_back(Tile(1, mid_x, mid_y));
        tiling(mid_x, x2, y1, mid_y, missing);
    } else if (X < mid_x && Y >= mid_y) { // Q3
        answer.push_back(Tile(2, mid_x, mid_y));
        tiling(x1, mid_x, mid_y, y2, missing);
    } else { // Q4
        answer.push_back(Tile(3, mid_x, mid_y));
        tiling(mid_x, x2, mid_y, y2, missing);
    }

    // Fill the other quadrants with a fake missing tile at their center
    if (missing != make_pair(mid_x, mid_y)) tiling(x1, mid_x, y1, mid_y, {mid_x - 1, mid_y - 1});
    if (missing != make_pair(mid_x + 1, mid_y)) tiling(mid_x, x2, y1, mid_y, {mid_x, mid_y - 1});
    if (missing != make_pair(mid_x, mid_y + 1)) tiling(x1, mid_x, mid_y, y2, {mid_x - 1, mid_y});
    if (missing != make_pair(mid_x + 1, mid_y + 1)) tiling(mid_x, x2, mid_y, y2, {mid_x, mid_y});
}

int main() {
    int n, x, y;
    cin >> n >> x >> y;

    // Recursively tile the given square
    tiling(0, n, 0, n, {x, y});

    cout << answer.size() << endl;
    for (const auto &tile : answer) {
        cout << tile.type << " " << tile.x << " " << tile.y << endl;
    }

    return 0;
}
