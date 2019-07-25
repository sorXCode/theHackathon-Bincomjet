pragma solidity >=0.4.25 <0.6.0;
pragma experimental ABIEncoderV2;

contract InsureMe
{
    enum StateType{
        Registered,
        ObtainedPolicy,
        PolicyActive,
        Claim,
        PolicyClosed
    }

    struct User{
        string BVN;
        mapping (string => string) description;
    }

    struct UsersIndex{
        User user;
        int idPosition;
    }

    struct VehicleDescription{
        int avg_maintenance;
        string chassis_num;
        int cost_price;
        string date_of_purchase;
        bytes15 engine_num;
        int fuel_capacity;
        bool general_cartage;
        bool goods_only;
        int milage;
        string model;
        bool passengers_only;
        string purpose;
        int[] reg_no;
        string vehicle_faults;
        string vehicle_type;
        }

    struct VehiclesIndex{
        VehicleDescription Desc;
        int idPosition;
    }
    
    
    mapping (address => Userprofile) Users;
    mapping (string => Userprofile) UsersByBVN;
    mapping (address => VehicleDescription) InsuredVehicle;
    mapping (bytes15 => VehiclesIndex) Vechicles;

    mapping (address => string) public InstanceInsurer;
    mapping (address => bool) public InsurersList;
    address[] public UsersList;
    bytes15[] public InsuredVechiclesEngNum;
    // address public InstanceInsurer

    StateType public State;
    string public name;
    int[] paySchedule;

    int Premium;
    
    constructor(string memory _insurerName) public {
        InstanceInsurer[msg.sender] = _insurerName;
        InsurersList[msg.sender] = true;
    }
    
    modifier onlyInsurer() {
        require(InsurersList[msg.sender]);
        _;
    }
    
    modifier onlyUser() {
        require(!InsurersList[msg.sender]);
        _;
    }
    
    modifier checkUsersRecord(){
        //implement this if user record exists escape
        _;
    }
    
    function registerProfile(string memory _first_name,
        string memory _last_name,
        string memory _other_name,
        string memory _phone,
        string memory _email,
        string memory _BVN,
        string memory _username,
        string memory _sex) onlyUser checkUsersRecord public
    {
        address InstanceUser;

        InstanceUser = msg.sender;
        Users[InstanceUser].first_name = _first_name;
        Users[InstanceUser].last_name = _last_name;
        Users[InstanceUser].other_name = _other_name;
        Users[InstanceUser].phone = _phone;
        Users[InstanceUser].email = _email;
        Users[InstanceUser].BVN = _BVN;
        Users[InstanceUser].username = _username;
        Users[InstanceUser].sex = _sex;
        Users[InstanceUser].date = now;
        UsersList.push(InstanceUser) -1;
        UsersByBVN[_BVN] = Users[InstanceUser];
        State = StateType.Registered;

    }


    function getUsers() onlyInsurer public view returns(address[] memory) {
        require( UsersList.length > 0, "onlyInsurer allowed to use this");
        return UsersList;
    }
    
    function getUser(address _userAddress) onlyInsurer public view returns (Userprofile memory){
        return Users[_userAddress];
    }


    function payPremium(int amount, bool _status)  public  returns (bool){
        require(amount == Premium);
        require (_status == true, "Payment was Unsuceessful");
        Premium -= amount;
    }


    function getVehicleQuote() public view returns (int) {
        //logic of evaluation here
        return Premium;
    }

    modifier checkrecord(string memory _engine_num) {
        require(InsuredVechiclesEngNum.length > 0);
        
        _;
    }

    function getVehiclePolicy() public returns (bytes10){
        Premium = getVehicleQuote();
        
    }
}