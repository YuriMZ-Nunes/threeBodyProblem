#include <vector>
#include <cmath>

using namespace std;

const float G = 0.1;
const float MIN_DISTANCE = 100;

struct Vector2D {
    float x;
    float y;
};

class GravityObject
{
    Vector2D pos;
    Vector2D vel;
    float strength;

public:
    GravityObject(float posX, float posY, double vx, double vy, float strength)
    {
        pos.x = posX;
        pos.y = posY;
        vel.x = vx;
        vel.y = vy;
        this->strength = strength;
    }

    Vector2D getPos()
    {
        return pos;
    }

    float getStrength()
    {
        return strength;
    }

    void updatePhysics(std::vector<GravityObject>& objects) {
        Vector2D totalForce = { 0, 0 };

        for (auto& objs : objects) {
            if (&objs == this) continue;

            Vector2D delta = {
                objs.getPos().x - this->getPos().x,
                objs.getPos().y - this->getPos().y
            };
            float distance = sqrt(pow(delta.x, 2) + pow(delta.y, 2));

            if (distance < 100) {
                distance = 100;
                delta.x = delta.x * (100 / (distance + 0.01));
                delta.y = delta.y * (100 / (distance + 0.01));
            }

            float forceMagnitude = G * (this->getStrength() * objs.getStrength()) / pow(distance, 2);

            Vector2D force = {
                delta.x * (forceMagnitude / distance),
                delta.y * (forceMagnitude / distance)
            };

            totalForce.x += force.x;
            totalForce.y += force.y;
        }

        vel.x += totalForce.x * 0.1;
        vel.y += totalForce.y * 0.1;

        pos.x += vel.x * 0.1;
        pos.y += vel.y * 0.1;
    }

};

std::vector<GravityObject> objects;

extern "C" {
    void addObject(float x, float y, float vX, float vY, float strength) {
        objects.push_back(GravityObject(x, y, vX, vY, strength));
    }

    Vector2D iteratePhysic(int index) {
        objects[index].updatePhysics(objects);
        return objects[index].getPos();
    }
}

