package config

var AllRoles = map[string][]string{
	"user":  {},
	"admin": {"getUsers", "manageUsers"},
}

var Roles = getKeys(AllRoles)
var RoleRights = AllRoles

func getKeys(m map[string][]string) []string {
	keys := make([]string, 0, len(m))
	for k := range m {
		keys = append(keys, k)
	}
	return keys
}

// coming-soon features ( need to update it but i lazy so i decided not to use it. john, if you see this please fix this and use it ok? )
func UpdateRolePermissions(role string, newRights []string) {
	if _, exists := RoleRights[role]; !exists {
		RoleRights[role] = []string{}
	}
	RoleRights[role] = append(RoleRights[role], newRights...)
}
